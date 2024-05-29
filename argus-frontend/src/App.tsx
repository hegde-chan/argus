import React from 'react';
import logo from './logo.svg';
import './App.css';
import {Button} from "@mui/material";
import {JobProgressIndicator} from "./JobProgressIndicator";

function App() {
  return (
    <div className="App">
        <header className="App-header">
            <p>
                Welcome to Argus!
            </p>

            <div className="App-body">
                <JobProgressIndicator/>
            </div>
        </header>
    </div>
  );
}

export default App;
