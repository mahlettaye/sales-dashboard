//import * as React from 'react';
import React,{useState, useEffect} from 'react';
import { useTheme } from '@mui/material/styles';
import { LineChart, Line, XAxis, YAxis, Label, ResponsiveContainer } from 'recharts';
import Title from './Title';
import axios from 'axios'





// // function Getdata(){

// // const [initialdata, setinitialdata]=useState([{}])
// // useEffect(() => {
// //   fetch('/api').then(response =>response.json()).then(data => console.log(data))
  
 
// // });
// // return data
// // }

// // Generate Sales Data
// function createData(time, amount) {
//   return { time, amount };
// }

// const data = [
//   createData('00:00', 0),
//   createData('03:00', 300),
//   createData('06:00', 600),
//   createData('09:00', 800),
//   createData('12:00', 1500),
//   createData('15:00', 2000),
//   createData('18:00', 2400),
//   createData('21:00', 2400),
//   createData('24:00', undefined),
// ];



export default function Chart() {
//   const [initialdata, setinitialdata]=useState([{}])
//   useEffect(() => {
//     axios.get('http://localhost:5000/').then(response => {
//       console.log("SUCCESS", response)
//       setinitialdata(response)
//     }).catch(error => {
//       console.log(error)
//     })
//   //fetch('/api').then(response =>response.json()).then(data => console.log(data))
  
 
//   }, []);
//   const theme = useTheme();

   return (
      <React.Fragment>
       <Title>Today</Title>
       <ResponsiveContainer>
       
       </ResponsiveContainer>
     </React.Fragment>
);
}
