import { useState } from "react";
import "./Header.scss";
function Header() {
  const [todo, setTodo] = useState("");

  const handleAdd = () => {
    if (!todo.trim()) return;

    console.log("New Todo:", todo);
    setTodo("");
  };

  return (
    <header className="header">
      <h1>Todo App</h1>

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
    </header>
  );
}

export default Header;