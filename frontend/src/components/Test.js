import React, {useEffect, useState} from "react";
import client from "../services/client";

function Test(){
  const [todo, setTodo] = useState('');

  useEffect(()=>{
    client.get('todo/').then(res=> setTodo(res.data.message));   // to get the details from todo table
  },[])

  return (
    <div>
      <ul>
        {
          console.log(todo)
        }
          </ul>  
    </div>
  );
}

export default Test;