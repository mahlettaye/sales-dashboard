
import React, { useEffect, useState } from 'react';
import axios from 'axios'

function Chart() {
  const [getMessage, setGetMessage] = useState({})

  useEffect(()=>{
    axios.get('http://localhost:5000/').then(response => {
      console.log("SUCCESS", response)
      setGetMessage(response)
    }).catch(error => {
      console.log(error)
    })

  }, [])
  
  return (
    <div className="Chart">
      <header className="Chart-header">
       
        <p>React + Flask Tutorial</p>
        <div>{getMessage.status === 200 ? 
         
          <h3>{getMessage.data.Sales}</h3>
          :
          <h3>LOADING</h3>}</div>
      </header>
    </div>
  );
}

export default Chart;