import React from 'react';
//import Form from './components/form/form';
import logo from './images/logo.png';
import Ml from './components/ml/ml';
import './App.css';

function App() {
  return (
    <div className="App">
      <Ml />
      {/*
      <Form />
      */}
      <img src={logo} />
      <div className="powered">powered by</div>
      <p className="ml">Machine Learning</p>
    </div>
  );
}

export default App;
