Requirements

1. In order to fetch items based on the current query, you should send a GET request to the
   mocked https://example.com/api/items endpoint. The endpoint requires a query parameter q that is meant to hold the
   query’s value. The endpoint will fail if the q query parameter is not provided.

   
2. The component should render a ```div``` element that has the class name ```wrapper``` and two child elements:
   - A ```div``` element with the class name ```control```.
   - A ```div``` element with the class name ```list```.
   The ```div``` element with class name control should contain an input element with the class name ```input```, and this is the
   input in which the user enters a query.

3. Once a response comes from the API, all strings from the response should be displayed inside the ```div``` element with
   class name ```list```, each one inside a separate an element with the class name ```list-item```. The strings should be displayed
   in the same order as they arrived from the API.


4. You should avoid sending too many requests to the API; in particular, do not send requests on every single keypress!
   You are expected to properly debounce the requests. The debounce time-out should be 500 milliseconds.


5. When items are being fetched, a class name ```is-loading``` should be added to the input’s wrapper (the element with class
   name ```control```).


6. When items are being fetched, no request has been sent or the endpoint has returned zero items, the ```div``` element with
   class name ```list``` should not be rendered.

7. The component accepts the prop ```onSelectItem: (item: string) => void```, which should be called with an item when the
   user clicks on it. Clicking on an item does not have any side effect apart from calling the callback.

8. The component should be the default export and can be either a function component or a class component.

Assumptions

- https://example.com is a mocked service — it can be accessed only in the Codility UI.
- The mocked endpoint https://example.com/api/items returns an array of strings. The array’s length is at most 10.
- Assume that a request sent to the mocked endpoint https://example.com/api/items never fails when provided a q query
parameter.
- The “Preview” tab will display your component. You can use it for testing purposes. In preview mode, the API is mocked
up, and will always return a random valid result. Also, the preview page imports a CSS spreadsheet from Bulma (v0.7.5)
to provide some styling.
- Design/styling is not assessed and will not affect your score. You should focus only on implementing the requirements.
- Use ```console.log``` and ```console.error``` for debugging purposes via your browser’s developer tools.
- When using Axios you are expected to use ```params``` argument and not build the URL by hand (documentation).

Additional examples

Example 1

Let’s consider the following sequence of actions:

- The user types “q” into the input;
- After 50 ms the user presses “u”, and then again, after every 50 ms, a new character is inserted until the input value
is “query”;
- Only one request to the API is sent, exactly 500 ms after “y” is input;
- During this period (from pressing “y” until the response comes in), the class name is-loading is added to the input’s
wrapper.

Example 2

If the response from the API endpoint is:

```
["Italy", "Spain", "Portugal", "Macedonia"]
```

then the list section, which is rendered as follows:

```
<div class="list">
  <a class="list-item">Italy</a>
  <a class="list-item">Spain</a>
  <a class="list-item">Portugal</a>
  <a class="list-item">Macedonia</a>
</div>
```

Available packages/libraries

- react (v18.2.0)
- typescript (v5.3.3)
- classnames (v2.5.1)
- lodash (v4.17.21)
- axios (v1.6.2)