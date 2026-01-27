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
  return (
    <div className="w-screen h-screen bg-amber-100 flex justify-center p6">
      <div className="w-[500px]">
        <h1 className="text-3xl text-green-700 font-bold text-center">
          Gerenciador de tarefas
        </h1>
        <AddTask />
        <Tasks tasks={tasks}/>
      </div>
    </div>
  );
}

export default App;