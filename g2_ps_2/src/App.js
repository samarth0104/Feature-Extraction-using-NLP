import React, { useState, useEffect } from 'react';
import Data from './csv_files/survey_responses_sorted.csv';
import Papa from 'papaparse';
import './App.css';
import anonImage from './images/anon.jpg'; // Import your anonymous image
import Statistics from './components/Statistics'; // Import Statistics component
import CustomPieChart from './components/PieChart';
import Reviews from './components/Reviews'; // Import Reviews component
import Feature from './components/Feature';

function App() {
  const [data, setData] = useState([]);
  const [productName, setProductName] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch(Data);
      const reader = response.body.getReader();
      const result = await reader.read();
      const decoder = new TextDecoder("utf-8");
      const csvData = decoder.decode(result.value);
      const parsedData = Papa.parse(csvData, {
        header: true,
        skipEmptyLines: true
      }).data;
      setData(parsedData);

      if (parsedData.length > 0) {
        setProductName(parsedData[0].product_name);
      }
    };
    fetchData();
    document.title = "G2 Marketing Solutions";
  }, []);

  // Function to chunk the array into groups of size n
  const chunkArray = (arr, n) => {
    const chunkedArray = [];
    for (let i = 0; i < arr.length; i += n) {
      chunkedArray.push(arr.slice(i, i + n));
    }
    return chunkedArray;
  };

  // Chunk the data array into groups of 2
  const chunkedData = chunkArray(data.slice(0, 3), 3);

  return (
    <div className="App">
      <div style={{ width: '100%', height: '70px', background: 'black', marginBottom: '-100px', display: 'flex', alignItems: 'center', justifyContent: 'flex-start' }}>
        <h2 style={{ color: 'orange', fontWeight: 'bold', marginLeft: '20px' }}>{productName}</h2>
        <img
          src={getImageUrl('https://sonarsoftware.com/wp-content/uploads/2021/10/G2-logo.png')} // Replace comment-icon.png with your actual image URL
          alt="Logo"
          style={{
            position: 'absolute',
            top: 0,
            right: 0,
            width: '65px',
            height: '70px',
            background: 'transparent'
          }}
        />
      </div>
      <div style={{ width: '100%', height: '70px', background: 'orange', marginBottom: '20px', display: 'flex', alignItems: 'center', justifyContent: 'flex-start', marginTop: '100px' }}>
        <h2 style={{ color: 'black', fontWeight: 'bold', marginLeft: '20px' }}>Feature Set</h2>
      </div>
      <Feature />

      <div style={{ width: '100%', height: '70px', background: 'black', marginBottom: '20px', display: 'flex', alignItems: 'center', justifyContent: 'flex-start', marginTop: '150px' }}>
        <h2 style={{ color: 'orange', fontWeight: 'bold', marginLeft: '20px' }}>Stats of all the reviews</h2>
      </div>
      <div className="product-container" style={{ position: 'relative', marginLeft: '30px' }}>
        <div>
          <div className="horizontal-container">
            <CustomPieChart data={data} />
            {/* Render Statistics component */}
            <Statistics data={data} />
          </div>
        </div>
      </div>
      <div style={{ width: '100%', height: '70px', background: 'black', marginBottom: '20px', display: 'flex', alignItems: 'center', justifyContent: 'flex-start', marginTop: '100px' }}>
        <h2 style={{ color: 'orange', fontWeight: 'bold', marginLeft: '20px' }}>Top Reviews</h2>
      </div>
      {/* Render Reviews component */}
      <Reviews chunkedData={chunkedData} />
    </div>
  );
}

function getImageUrl(url) {
  if (!url || !(url.endsWith('.jpg') || url.endsWith('.jpeg') || url.endsWith('.png'))) {
    return anonImage;
  }
  return url;
}

export default App;
