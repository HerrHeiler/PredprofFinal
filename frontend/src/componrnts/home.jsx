import React, { useState, useEffect } from 'react';
import axios from 'axios';

const HomePage = () => {
    const [data, setData] = useState(null); // данные который приходят с бэка
    const [loading, setLoading] = useState(true); // сост. загрузки
    const [error, setError] = useState(null); // ошиби
  //начало
    useEffect(() => {
      const fetchData = async () => {
        try {
          //Post-запрос
          const response = await axios.post('http://localhost:5000/home');
        if (response.data.succes) {
          setData(response.data.items); // обновляю datу 
        } else {
        
          setError(response.data.message);
        }

        } catch (err) {
          setError(err.message);

        } finally {
          setLoading(false);
        }
      };
      fetchData();
    }, []);
    if (loading) return <div>Загрузка ХАХАХАХА</div>
    if (error) return <div>Ошибка, лох: {error}</div>
    console.log(data, "prsadawd")
    return (
      <div style={{marginLeft: "auto", marginRight: "auto" }}>
        <h1 sryle= {{justifyContent: "center", marginLeft: "auto", marginRight: "auto"}}>Карта</h1>
        {Object.entries(data).map(([indy, heights]) => ( // entries создает массив пар значений
        <div key={indy} style={{padding: "5px", justifyContent: "center", marginLeft: "auto", marginRight: "auto"}}>
          {heights.map((heightsh, heightsIndex) => (
            <div key={heightsIndex} style={{}}>
              {heightsh.map((height, heightIndex) => (
                <div
                key={heightIndex}
                style={{
                  width: '6.5px',
                      height: '10px',
                      borderRadius: '4px',
                      backgroundColor: "red",
                      opacity: height/255,
                      float: "left",
                      marginLeft: "auto", 
                      marginRight: "auto"

                }}
                />
              ))}
            </div>
          ))}
        </div>
        ))}
      </div>
  )
};

export default HomePage