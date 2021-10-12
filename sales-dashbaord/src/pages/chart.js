import React, { useEffect, useState } from 'react';

import { useTheme } from '@mui/material/styles';
import { makeStyles } from "@material-ui/core/styles";

import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import TablePagination from "@material-ui/core/TablePagination";
import Title from './Title';


class LTable extends React.Component {
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
   const useStyles = makeStyles({
    table: {
      minWidth: 650
    }
  });
   function preventDefault(event) {
      event.preventDefault();
    }
    const classes = useStyles();
    const [page, setPage] = React.useState(0);
    const [rowsPerPage, setRowsPerPage] = React.useState(10);
    const handleChangePage = (event, newPage) => {
      setPage(newPage);
    };

    const handleChangeRowsPerPage = event => {
      setRowsPerPage(parseInt(event.target.value, 10));
      setPage(0);
    };
    const emptyRows =
      rowsPerPage - Math.min(rowsPerPage, contacts.length - page * rowsPerPage);
    
   return (
   <div>
       <React.Fragment>
       <Title>Sales Data</Title>
       <Table size="small">
         <TableHead>
           <TableRow>
             <TableCell>Store</TableCell>
             <TableCell>Date</TableCell>
             <TableCell>Consumers</TableCell>
             <TableCell>StateHoliday</TableCell>
             <TableCell>SchoolHoliday</TableCell>
             
             <TableCell align="right">Sale Amount</TableCell>
           </TableRow>
         </TableHead>
         
         <TableBody>
           {contacts.slice(page* rowsPerPage, page * rowsPerPage + rowsPerPage).map((row,index) => (
             <TableRow key={row.SalesID}>

               <TableCell >{row.Store}</TableCell>
               <TableCell >{row.Date}</TableCell>
               <TableCell >{row.Customers}</TableCell>
               <TableCell >{row.StateHoliday}</TableCell>
               <TableCell >{row.SchoolHoliday}</TableCell>
             
               
               <TableCell align="right">{`$${row.Sales}`}</TableCell>
             </TableRow>
           ))}
           {emptyRows > 0 && (
            <TableRow style={{ height: 53 * emptyRows }}>
              <TableCell colSpan={6} />
            </TableRow>
          )}
         </TableBody>
         
       </Table>
       <TablePagination
        rowsPerPageOptions={[5, 10, 25]}
        component="div"
        count={contacts.length}
        rowsPerPage={rowsPerPage}
        page={page}
        onChangePage={handleChangePage}
        onChangeRowsPerPage={handleChangeRowsPerPage}
      />
       
     </React.Fragment>
       
       
       
       
       
       

       
       
   </div>
   )
};
export default LTable