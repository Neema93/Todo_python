import { useEffect, useState } from "react";
import axios from "axios";

import Header from "./components/Header";
import TodoList from "./components/TodoList";

function App() {
  const [tasks, setTasks] = useState([]);

  const fetchTasks = async () => {
    const res = await axios.get("http://localhost:8000/tasks");
    setTasks(res.data);
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  const handleDelete = async (id) => {
    await axios.delete(`http://localhost:8000/task/${id}`);
    fetchTasks();
  };

  const handleToggle = async (task) => {
    await axios.put(`http://localhost:8000/task/${task.id}`, {
      name: task.name,
      checked: !task.checked,
    });

    fetchTasks();
  };

  return (
    <div className="app">
      <Header onAdd={fetchTasks} />

      <TodoList
        tasks={tasks}
        onDelete={handleDelete}
        onToggle={handleToggle}
      />
    </div>
  );
}

export default App;