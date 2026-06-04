export default function TodoItem({ task, onDelete, onToggle }) {
  return (
    <div className="todo-item">
      <div className="left">
        <input
          type="checkbox"
          checked={task.checked}
          onChange={() => onToggle(task)}
        />

        <span
          style={{
            textDecoration: task.checked ? "line-through" : "none",
          }}
        >
          {task.name}
        </span>
      </div>

      <div className="actions">
        <button
          className="update-btn"
          onClick={() => onToggle(task)}
        >
          Update
        </button>

        <button
          className="delete-btn"
          onClick={() => onDelete(task.id)}
        >
          Delete
        </button>
      </div>
    </div>
  );
}