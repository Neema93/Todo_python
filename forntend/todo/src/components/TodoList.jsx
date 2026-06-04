import TodoItem from "./TodoItem";
import'./TodoList.scss';
export default function TodoList({ tasks, onDelete, onToggle }) {
  return (
    <div className="todo-list">
      {tasks.map((task) => (
        <TodoItem
          key={task.id}
          task={task}
          onDelete={onDelete}
          onToggle={onToggle}
        />
      ))}
    </div>
  );
}