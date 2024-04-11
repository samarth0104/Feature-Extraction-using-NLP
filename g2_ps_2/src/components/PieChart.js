import React, { Component } from 'react';
import CanvasJSReact from '@canvasjs/react-charts';

var CanvasJSChart = CanvasJSReact.CanvasJSChart;

class App extends Component {
    render() {
        // Calculate the counts for each category
        const positiveCount = this.props.data.filter(review => parseFloat(review.star_rating) > 3).length;
        const neutralCount = this.props.data.filter(review => parseFloat(review.star_rating) === 3).length;
        const negativeCount = this.props.data.filter(review => parseFloat(review.star_rating) < 3).length;

        // Prepare data for pie chart
        const pieData = [
            { name: 'Positive', value: positiveCount },
            { name: 'Neutral', value: neutralCount },
            { name: 'Negative', value: negativeCount }
        ];

        // Calculate total count
        const totalCount = positiveCount + neutralCount + negativeCount;

        // Convert counts to percentages
        const dataPoints = pieData.map(({ name, value }) => ({ y: (value / totalCount * 100).toFixed(2), label: name }));

        const options = {
            exportEnabled: false,
            animationEnabled: true,
            title: {
                text: "Reviwes Distribution",
                fontFamily: "Arial, sans-serif", // Specify the font family here
            },
            data: [{
                type: "pie",
                startAngle: 75,
                toolTipContent: "<b>{label}</b>: {y}%",
                showInLegend: true,
                legendText: "{label}",
                indexLabelFontSize: 16,
                indexLabel: "{label} - {y}%",
                dataPoints: dataPoints
            }]
        };

        return (
            <div>
                <CanvasJSChart options={options} />
            </div>
        );
    }
}

export default App;
