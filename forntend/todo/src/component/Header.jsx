import { useState } from "react";
import "./Header.scss";
import Todoinput from "./Todoinput";
function Header() {
  

  return (
    <header className="header">
      <h1>Todo App</h1>
    <Todoinput />
    </header>
  );
}

export default Header;