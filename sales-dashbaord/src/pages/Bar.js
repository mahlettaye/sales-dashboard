import React, { useEffect, useState } from 'react';
import { PieChart, Pie, Sector, Tooltip,
    Legend,ResponsiveContainer } from 'recharts';

import { useTheme } from '@mui/material/styles';


import Title from './Title';


class Bar extends React.Component {
   state = {
     contacts: []
     
   };
   render() {
     return (
       <Contacts contacts={this.state.contacts} />
   )
   }
   componentDidMount() {
     fetch('http://localhost:5000/')
     .then(res => res.json())
     .then(data => {
     this.setState({ contacts: data });
   })
   .catch(console.log);
}
 }
 const Contacts = ({ contacts }) => {
   const theme = useTheme();
   function preventDefault(event) {
      event.preventDefault();
    }

  
    const newData = contacts.reduce(
        (acc, el) => {
            acc[el['SchoolHoliday']] = (acc[el['SchoolHoliday']] || 0) + 1;
            return acc;
        },
        {}
    );
    const codes = Object.entries(newData)
      .map(([key, value]) => {
          return {SchoolHoliday: key, count: value};
      });   
   

      
    
     
    
    
   return (
 
   
    
   
   <div>
       <React.Fragment>
      <Title>Today</Title>
      
        
        <ResponsiveContainer width="100%" height={200}>
        <PieChart width={400} height={400}>
          <Pie
            dataKey="count"
            isAnimationActive={false}
            data={codes}
            cx="50%"
            cy="50%"
            outerRadius={80}
            fill="#8884d8"
            label
          />
        
          <Pie dataKey="Sales" data={contacts} cx={500} cy={200} innerRadius={40} outerRadius={80} fill="#82ca9d" />
          <Tooltip />
         
        </PieChart>
        </ResponsiveContainer>

        
    </React.Fragment>
       
       
       
       
       
       

       
       
   </div>
   )
};
export default Bar