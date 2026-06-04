import { useState } from "react";
import axios from "axios";
import "./Todoinput.scss";

export default function Todoinput({ onAdd }) {
  const [todo, setTodo] = useState("");

  const handleAdd = async () => {
    if (!todo.trim()) return;

    try {
      const res = await axios.post("http://localhost:8000/task", {
        name: todo,
        checked: false,
      });

      console.log("Added:", res.data);

      if (onAdd) onAdd(); // refresh list in parent

      setTodo("");
    } catch (err) {
      console.error("Error adding todo:", err);
    }
  };

  return (
    <div className="todo-input">
      <input
        type="text"
        placeholder="Enter a task..."
        value={todo}
        onChange={(e) => setTodo(e.target.value)}
      />

      <button onClick={handleAdd}>Add</button>
    </div>
  );
}