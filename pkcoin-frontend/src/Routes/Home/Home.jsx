import React, { useEffect, useState } from 'react';

// Import CSS
import '../App/App.css';
import './Home.css';

import Header from '../Header/Header';
import Card from '../Cards/Card';

import request from 'request';

export default Home;

let PrevHash = 100;
let CurHash = PrevHash;
let nonce = 100;
let time = 0;

function Home() {

  let [chain, setChain] = useState();
  let [diff, setDiff] = useState();
  let [miningReward, setMiningReward] = useState();
  let [pendingTransactions, setPending] = useState();

  useEffect(() =>
  {
    request('http://127.0.0.1:5000/get_blockchain', (err, res, body) =>
    {
      let PKcoin = JSON.parse(body);
      setChain(PKcoin.chain);
      setDiff(PKcoin.diff);
      setMiningReward(PKcoin.miningReward);
      setPending(PKcoin.pendingTransactions);
    });
  }, []);

  return (
    <div className="App">
      <Header/>
      <div className="content-container">
        <h1> Hello </h1>
        {chain}
        <p> Here are some transactions... </p>
        <ul className="card-container">
          <Card blockNo={1} PrevHash={PrevHash} CurHash={CurHash} time={time} nonce={nonce} />
          <Card blockNo={2} PrevHash={PrevHash} CurHash={CurHash} time={time} nonce={nonce} />
        </ul>

      </div>
    </div>
  );
}
