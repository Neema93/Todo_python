
import "./Header.scss";
import Todoinput from "./Todoinput";
export default function Header({ onAdd }) {
  return (
    <header className="header">
      <h1>Todo App</h1>
      <Todoinput onAdd={onAdd} />
    </header>
  );
}
