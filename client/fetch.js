async function fetchDataJSON() {
  const response = await fetch('http://127.0.0.1:8000/');
  const data = await response.json();
  console.log(data);
  return data;
}
fetchDataJSON().then(data => {
  data; // fetched data
});