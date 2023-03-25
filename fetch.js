async function fetchDataJSON() {
    const response = await fetch('http://127.0.0.1:8000/bus/orders');
    const data = await response.json();
    return data;
  }
  
  fetchDataJSON().then(data => {
    const table = document.querySelector('#orderData');
  
    // create table header
    const headerRow = table.insertRow();
    Object.keys(data[0]).forEach(key => {
      const headerCell = document.createElement('th');
      const text = document.createTextNode(key);
      headerCell.appendChild(text);
      headerRow.appendChild(headerCell);
    });
  
    // populate table rows
    data.forEach(order => {
      const row = table.insertRow();
      Object.values(order).forEach(value => {
        const cell = row.insertCell();
        const text = document.createTextNode(value);
        cell.appendChild(text);
      });
    });
  });


  window.onload = async function() {
    const data = await fetchDataJSON();
    const orderData = document.querySelector("#orderData");
  
    data.forEach(order => {
      const newRow = orderData.insertRow(-1); // insert new row at the end of the table
      newRow.insertCell(0).innerHTML = order._oID;
      newRow.insertCell(1).innerHTML = order._custName;
      newRow.insertCell(2).innerHTML = order._busName;
      newRow.insertCell(3).innerHTML = new Date(order._date).toLocaleString();
      newRow.insertCell(4).innerHTML = order._total;
    });
  };
  