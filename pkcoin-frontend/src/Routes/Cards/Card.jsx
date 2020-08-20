import React from 'react';

// Import CSS
import '../App/App.css';
import '../Home/Home.css';
import './Card.css';

export default Card;

function Card(props)
{
  let hmm = '';
  if (props.blockNo === 1)
  {
    hmm = '(Genesis block)';
    if (props.PrevHash === '')
    {
      props.PrevHash = 0;
    }
  }

  return (
    
    <div className="card" id={props.blockNo - 1} >
      <card-body>
      <h3> Block {props.blockNo} </h3> {hmm}
      </card-body>
      <list-items>
      Previous hash<br></br><oo>{props.PrevHash}</oo>
      <br></br><br></br>
      Current hash<br></br><oo>{props.CurHash}</oo>
      </list-items>
      <list-items>
      Key<br></br><it>{props.nonce}</it>
      </list-items>
      <list-items-bruh>
      Timestamp<br></br><it>{props.time}</it>
      </list-items-bruh>
    </div>
  );
}