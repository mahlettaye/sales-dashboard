import React from 'react';
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  Brush,
  AreaChart,
  Area,
  ResponsiveContainer,
} from 'recharts';
import { useTheme } from '@mui/material/styles';


import Title from './Title';


class Chart extends React.Component {
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
          acc[el['Month']] = (acc[el['Month']] || 0) + 1;
          return acc;
      },
      {}
  );
  const codes = Object.entries(newData)
    .map(([key, value]) => {
        return {StateHoliday: key, count: value};
    });
    const renderLabel = (prop, dataKey) => {
      const index = prop.index;
      const target = codes[index];
      const highlights = target.highlights || [];
    
      if (highlights.length > 0) {
        for (let i = 0; i < highlights.length; i++) {
          if (highlights[i].key === dataKey) {
            return highlights[i].marker;
          }
        }
      }
    };
    
   return (
   <div>
       <React.Fragment>
      <Title>Sales per Month</Title>        
        <ResponsiveContainer width="100%" height={200}>
          <LineChart
            width={500}
            height={200}
            data={contacts}
            syncId="anyId"
            margin={{
              top: 10,
              right: 30,
              left: 0,
              bottom: 0,
            }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="Month" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Line type="monotone" dataKey="Sales" stroke="#82ca9d" fill="#82ca9d" />
            <Brush />
          </LineChart>
        </ResponsiveContainer>

        
    </React.Fragment>
       
       
       
       
       
       

       
       
   </div>
   )
};
export default Chart