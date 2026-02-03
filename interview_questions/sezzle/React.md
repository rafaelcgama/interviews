1. API REQUIREMENTS

- Use the endpoint provided in the test (ITEMS_API_URL).
- The request must be done with axios.
- The query must be passed as axios params, like:

```
axios.get(ITEMS_API_URL, { params: { q: value } })
```

- Response is an array of strings.
- If the request fails, the list should become empty.

---

2. REACT COMPONENT REQUIREMENTS

Component name: Autocomplete
Props:
-	onSelectItem(item: string)

State you must handle:
-	query/text (the input value)
-	items (list returned from the server)
-	loading (controls spinner)

Behavior:
1.	Every time the user types, update the query state.
2.	Wait 500ms debounce before sending the request.
3.	Cancel previous calls implicitly through debounce (not manually).
4.	Do NOT send requests on every keypress — debounce is mandatory.
5. If the input is empty:
    - Do not fetch
    - Clear items
    - loading = false
6.	When clicking a list item, call onSelectItem(item).
7.	Do not render the list when loading.
8.	Do not render the list when items array is empty.

---

3. ALLOWED LIBRARIES

- React
- axios
- lodash


---

4. DEBOUNCE REQUIREMENTS

• Debounce delay must be 500 ms
• Must wrap the fetch function with _.debounce
• Only one request is allowed after the user stops typing
• Must appear in the rendered behavior (Codility tests check this)

---

5. HTML / CSS CLASS REQUIREMENTS

The DOM structure and classes must match exactly:

```
<div class="wrapper">
  <div class="control is-loading">
    <input class="input" />
  </div>

  <div class="list">
    <a class="list-item">Item</a>
    <a class="list-item">Item 2</a>
  </div>
</div>
```

Rules:

• wrapper wraps everything.
• control wraps the input.
• When loading, control must include "is-loading".
• Input must have class "input".
• List wrapper must be "list".
• Each result item must be an <a> with class "list-item".

Codility tests strictly check these class names.

---

6. VISIBILITY RULES

• Show the spinner (is-loading) only while waiting for the API.
• Hide the list when:
•	loading
•	query empty
•	items empty

• Show list only when:
•	not loading
•	items length > 0

⸻

7. RETURN VALUE / CALLBACK

• When a user clicks an item, call onSelectItem

---

8. WHAT YOU MUST NOT DO

• No custom fetch. No fetch().
• No libraries other than React, axios, lodash.
• No inline debounce implementation.
• No extra HTML tags.
• No extra classes beyond what was shown.
• No changing class names.
• No returning lists during loading.
• No requests when query is empty.