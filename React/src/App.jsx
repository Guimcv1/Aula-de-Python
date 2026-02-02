import AddTask from "./componenets/AddTask";
import Tasks from "./componenets/Tasks";
import { useState } from "react";


function App(){

  const [tasks, setTasks] = useState([
    {
    id: 1,
    title: "Estudar Programação",
    description: "Estudar programação para se tornar um desenvolvedor full stack",
    isCompleted: false,
    },
    {
    id: 2,
    title: "Estudar Matematica",
    description: "Estudar Matematica para se tornar um Einstein",
    isCompleted: false,
    },
    {
    id: 3,
    title: "Estudar Musculação",
    description: "Estudar Musculação para se tornar um Maromba full stack",
    isCompleted: false,
    },
  ]);

  function onTaskClick(taskId){
    const newTasks = tasks.map(tasks => {
      if (tasks.id == taskId){
        return {...tasks, isCompleted: !tasks.isCompleted}
      } 
      return tasks;

    })
  }

  return (
    <div className="w-screen h-screen bg-amber-100 flex justify-center p6">
      <div className="w-[500px]">
        <h1 className="text-3xl text-green-700 font-bold text-center ">
          Gerenciador de tarefas
        </h1>        
        <br/>
        <Tasks tasks={tasks} onTaskClick={onTaskClick}/>
      </div>
    </div>
  );
}

export default App;