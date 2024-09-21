import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from "react";

function BackendGreeting() {
  const [data, setData]  = useState({"message": "didn't work"});

  useEffect(() => {
    fetch('http://localhost:8000/')
    .then(response => response.json())
    .then(json => setData(json))
    .catch(error => console.error(error));
  }, []);

  return (
    <p> {data.message} </p> 
  );
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <BackendGreeting /> 
      </header>
    </div>
  );
}

export default App;
