import React from 'react';

// Import CSS
import '../App/App.css';
import './Home.css';

import Header from '../Header/Header';
import Card from '../Cards/Card';

export default Home;

let PrevHash = 100;
let CurHash = PrevHash;
let key = 100;
let time = 0;

function Home() {
  return (
    <div className="App">
      <Header/>

      <div className="content-container">

        <h1> Hello </h1>
        <p> Here are some transactions... </p>
        <div className="card-container">
          <Card blockNo={1} PrevHash={PrevHash} CurHash={CurHash} key={key} time={time} />
          <Card blockNo={2} PrevHash={PrevHash} CurHash={CurHash} key={key} time={time} />
        </div>

      </div>
    </div>
  );
}
