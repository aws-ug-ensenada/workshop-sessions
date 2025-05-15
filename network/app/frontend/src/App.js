import React, { useEffect, useState } from "react";
import { fetchData } from "./api";

function App() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    fetchData().then(setItems);
  }, []);

  return (
    <div>
      <h1>Items from MySQL</h1>
      <ul>
        {items.map((item) => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
