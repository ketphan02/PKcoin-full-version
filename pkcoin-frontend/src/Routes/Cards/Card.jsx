import React from 'react';

// Import CSS
import '../App/App.css';
import '../Home/Home.css';

export default Card;

function Card(props)
{
  let hmm = '';
  if (props.blockNo === 1)
  {
    hmm = '(Genesis block)';
  }

  return (
    
    <div className="card" id={props.blockNo - 1}>
      <card-body>
      <h3> Block {props.blockNo} </h3> {hmm}
      </card-body>
      <list-items>
      Previous hash<br></br>{props.PrevHash}
      <br></br><br></br>
      Current hash<br></br>{props.CurHash}
      </list-items>
      <list-items>
      Key<br></br>{props.nonce}
      </list-items>
      <list-items-bruh>
      Timestamp<br></br>{props.time}
      </list-items-bruh>
    </div>
  );
}