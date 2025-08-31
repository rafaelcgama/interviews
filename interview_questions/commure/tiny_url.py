import os
import base62
from flask import Flask, request, abort, jsonify, redirect
from urllib.parse import urlparse
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# ---- Flask ----
app = Flask(__name__)
DB_PATH = "data.db"

engine = create_engine(f"sqlite:///{DB_PATH}", future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)
Base = declarative_base()


class Url(Base):
    __tablename__ = "urls"
    id = Column(Integer, primary_key=True, autoincrement=True)
    original_url = Column(String, nullable=False, unique=True)
    # remaining_uses = Column(Integer, nullable=True)  # NULL => unlimited


def init_db():
    os.makedirs(os.path.dirname(DB_PATH) or ".", exist_ok=True)
    Base.metadata.create_all(bind=engine)


init_db()


# ---- helpers ----
def is_url(u: str) -> bool:
    try:
        p = urlparse(u)
        return p.scheme in {"http", "https"} and bool(p.netloc)
    except Exception:
        return False


# ---- API: create short link ----
@app.post("/api/shorten")
def new_link():
    data = request.get_json(silent=True)
    url = data.get("url").strip()
    # treat missing or blank remaining_uses as None (unlimited)
    remaining_uses = data.get("remaining_uses", None)

    if url is None:
        return jsonify({"error": "Missing 'url'"}), 400
    if is_url(url) is None:
        return jsonify({"error": "Invalid http(s) URL."}), 400

    with SessionLocal() as s:
        # reuse existing mapping if present
        obj = s.query(Url).filter(Url.original_url == url).one_or_none()
        if obj is None:
            obj = Url(original_url=url) #, remaining_uses=remaining_uses)
            s.add(obj)
            s.commit()
            s.refresh(obj)
        # (simplest behavior) if it exists, we DO NOT overwrite remaining_uses
        code = base62.encode(obj.id)

    short_url = f'{request.host_url.rstrip("/")}{"/"}{code}'  # make sure there is no //
    return jsonify({"short_url": short_url})


# ---- Redirect: use short link ----
@app.get("api/<code>")  # not use /api so it looks like a bitly
def get_code(code):
    url_id = base62.decode(code)

    with SessionLocal() as s:
        obj = s.get(Url, url_id)
        if obj is None:
            abort(404)

        # # enforce remaining uses (NULL => unlimited)
        # if obj.remaining_uses is not None:
        #     if obj.remaining_uses == 0:
        #         abort(410)  # Gone
        #     obj.remaining_uses -= 1
        #     s.commit()

        return redirect(obj.original_url, code=302)


if __name__ == "__main__":
    app.run(debug=True)
