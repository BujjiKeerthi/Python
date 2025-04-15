import { useState, useEffect } from "react";
function App() {
    const [speeds, setSpeeds] = useState([]); 
    const [data, setData] = useState(null);
  
    useEffect(() => {
      const fetchData = async () => {
        const speedParams = speeds.map((s) => `speed=${s}`).join("&"); 
        const url = `http://127.0.0.1:8000/steering/predict/?${speedParams}`;
  
        const response = await fetch(url);
        const jsonData = await response.json();
        // console.log(jsonData);
        setData(jsonData);
      };
  
      fetchData();
    }, [speeds]); 
  
    return (
      <div>
        <h1>Vehicle Control Data</h1>
  
      
        {data && data.predictions ? (
          <div>
            {data.predictions.map((prediction, index) => (
              <p key={index}>
                <strong>Speed:</strong> {prediction.speed},  
                <strong> Steering Angle:</strong> {prediction.predicted_steering_angle}
              </p>
            ))}
          </div>
        ) : (
          <p>Loading...</p>
        )}
  
       
        <input
          type="text"
          placeholder="Enter speeds (comma-separated)"
          onChange={(e) => {
            const newSpeeds = e.target.value.split(",").map(Number);
            setSpeeds(newSpeeds);
          }}
        />
      </div>
    );
  }

export default App;
