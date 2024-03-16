import React, { useState, useEffect } from 'react';
import ApexCharts from 'apexcharts';
import axios from 'axios';

const RiskScore = () => {
  const [anomalyCount, setAnomalyCount] = useState(60);

  useEffect(() => {
    const fetchAnomalyCount = async () => {
      try {
        const response = await axios.get('YOUR_API_ENDPOINT');
        const fetchedCount = response.data.anomalyCount; // Adjust according to your API response structure
        setAnomalyCount(fetchedCount);
      } catch (error) {
        console.error('Error fetching anomaly count:', error);
      }
    };

    fetchAnomalyCount();

    const interval = setInterval(fetchAnomalyCount, 5000);
    return () => clearInterval(interval);
  }, []);

  useEffect(() => {
    const options = {
      series: [anomalyCount],
      chart: {
        height: 350,
        type: 'radialBar',
        toolbar: {
          show: true
        }
      },
      plotOptions: {
        radialBar: {
          startAngle: -135,
          endAngle: 225,
          hollow: {
            margin: 0,
            size: '70%',
            background: '#fff',
            image: undefined,
            imageOffsetX: 0,
            imageOffsetY: 0,
            position: 'front',
            dropShadow: {
              enabled: true,
              top: 3,
              left: 0,
              blur: 4,
              opacity: 0.24
            }
          },
          track: {
            background: '#fff',
            strokeWidth: '67%',
            margin: 0,
            dropShadow: {
              enabled: true,
              top: -3,
              left: 0,
              blur: 4,
              opacity: 0.35
            }
          },
          dataLabels: {
            show: true,
            name: {
              offsetY: -10,
              show: true,
              color: '#888',
              fontSize: '17px'
            },
            value: {
              formatter: function(val) {
                return parseInt(val);
              },
              color: '#111',
              fontSize: '36px',
              show: true,
            }
          }
        }
      },
      fill: {
        type: 'gradient',
        gradient: {
          shade: 'dark',
          type: 'vertical',
          shadeIntensity: 0.5,
          gradientToColors: ['#7e2fed'],
          inverseColors: true,
          opacityFrom: 1,
          opacityTo: 1,
          stops: [0, 100]
        }
      },
      stroke: {
        lineCap: 'round'
      },
      labels: ['Percent'],
    };

    const chart = new ApexCharts(document.querySelector("#chart"), options);
    chart.render();
    return () => chart.destroy();
  }, [anomalyCount]);

  return (
    <div>
      <div id="chart"></div>
    </div>
  );
};

export default RiskScore;
