function Tasks(props) {
    console.log(props);
    return (
    <ul className="space-y-4 p-6 bg-slate-200 rounded-md shadow">
        {props.tasks.map((tasks)=> 
        <li key={tasks.id} className="flex">
        <button className="bg-slate-500 text-white p-2 rounded-md w-full">{tasks.title}</button>
        <button className="bg-slate-500 text-white p-2 rounded-md">Ver detalhes</button>
        </li>)}
        
    </ul>
);
}

export default Tasks;