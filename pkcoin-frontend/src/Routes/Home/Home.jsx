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
  
  let [chain,setChain] = useState([{}]);
  let [diff, setDiff] = useState(0);
  let [miningReward, setMiningReward] = useState(0);
  let [pendingTransactions, setPending] = useState([{}]);

  useEffect(() =>
  {
    
    fetch('http://127.0.0.1:5000/get_blockchain')
    .then(res => res.json())
    .then((PKcoin) =>
    {
      setChain(PKcoin['chain']);
      setDiff(PKcoin['diff']);
      setMiningReward(PKcoin['miningReward']);
    })
    .catch(err => {});

  }, []);

  function mineBlock()
  {
    fetch('http://127.0.0.1:5000/mine_blockchain')
    .then(res => res.json())
    .then((PKcoin) =>
    {
      setChain(PKcoin.chain);
      setDiff(PKcoin.diff);
      setMiningReward(PKcoin.miningReward);
    })
    .catch(err => {});
  }

  return (
    <div className="App">
      <Header/>
      <div className="content-container">
        <h1> Hello </h1>
        <p> Here are some transactions... </p>
        <div className="card-container">
          {
            chain.map((block, i) => <Card blockNo={i + 1} PrevHash={block.prevHash} CurHash={block.hash} time={block.datetime} nonce={block.key} />)
          }
        </div>

        <button onClick={mineBlock}> MINE </button>
      </div>
    </div>
  );
}