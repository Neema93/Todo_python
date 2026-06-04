
import './App.scss';
import Header from './component/Header';
function App() {
  return (
       <div className="container">
   <Header onAdd={fetchTasks} />
    </div>
  );
}

export default App;
