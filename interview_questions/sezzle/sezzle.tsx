// @ts-ignore
import React, { useState, useEffect } from "interview_questions/sezzle/sezzle";
// @ts-ignore
import axios from "axios";
// @ts-ignore
import lodash from "lodash";

const ITEMS_API_URL = "https://example.com/api/items";

const Autocomplete = ({ onSelectItem }) => {
    const [text, setText] = useState("");
    const [items, setItems] = useState([]);
    const [loading, setLoading] = useState(false);

    // 1. Normal function first
    // @ts-ignore
    const fetchItems = async (q) => {
        if (!q) {
            setItems([]);
            setLoading(false);
            return;
        }

        setLoading(true);

        try {
            const res = await axios.get(ITEMS_API_URL, { params: { q } });
            setItems(res.data || []);
        } catch {
            setItems([]);
        }

        setLoading(false);
    };

    // 2. Debounced wrapper (only once)
    const debouncedFetch = lodash.debounce(fetchItems, 500);

    // 3. Call debounced version when text changes
    useEffect(() => {
        debouncedFetch(text);
    }, [text]);

    return (
        <div className="wrapper">
            <div className={`control ${loading ? "is-loading" : ""}`}>
                <input
                    className="input"
                    value={text}
                    onChange={(e) => setText(e.target.value)}
                />
            </div>

            {!loading && items.length > 0 && (
                <div className="list">
                    {items.map((item, i) => (
                        <a
                            key={i}
                            className="list-item"
                            onClick={() => onSelectItem(item)}
                        >
                            {item}
                        </a>
                    ))}
                </div>
            )}
        </div>
    );
};

export default Autocomplete;