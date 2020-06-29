import React from 'react';
import logo from './images/logo.png';
import Machine from './components/ml/ml';
import './App.css';

function App() {
  return (
    <div className="App">
      <Machine />
      <img src={logo} alt="img" />
      <div className="powered">powered by</div>
      <p className="ml">Machine Learning</p>
    </div>
  );
}

export default App;
