import { useState } from "react";
import "./Todoinput.scss";
export default function Todoinput() {
const [todo, setTodo] = useState("");

  const handleAdd = () => {
    if (!todo.trim()) return;

    console.log("New Todo:", todo);
    setTodo("");
  };
  return (
   

      <div className="todo-input">
        <input
          type="text"
          placeholder="Enter a task..."
          value={todo}
          onChange={(e) => setTodo(e.target.value)}
        />

        <button onClick={handleAdd}>
          Add
        </button>
      </div>
   
  );

}