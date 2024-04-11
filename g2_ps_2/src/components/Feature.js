import React, { useState, useEffect } from 'react';
import Papa from 'papaparse';
import Data from 'C:/Users/samar/OneDrive/Desktop/PESU/Extra/G2/g2_ps_2/src/csv_files/result.csv';
import SurveyData from 'C:/Users/samar/OneDrive/Desktop/PESU/Extra/G2/g2_ps_2/src/csv_files//survey_responses.csv';

function Feature() {
    const [categories, setCategories] = useState([]);
    const [selectedCategory, setSelectedCategory] = useState(null);
    const [features, setFeatures] = useState([]);
    const [, setShowFileInput] = useState(true);
    const [surveyResponses, setSurveyResponses] = useState([]);
    const [selectedFeature, setSelectedFeature] = useState(null);

    useEffect(() => {
        // Function to read the features file when the component mounts
        const readFeaturesFile = async () => {
            try {
                const response = await fetch(Data);
                const csvData = await response.text();
                parseFeaturesCSV(csvData);
            } catch (error) {
                console.error('Error fetching or parsing features CSV:', error);
            }
        };

        // Function to read the survey responses file when the component mounts
        const readSurveyResponsesFile = async () => {
            try {
                const response = await fetch(SurveyData);
                const csvData = await response.text();
                parseSurveyResponsesCSV(csvData);
            } catch (error) {
                console.error('Error fetching or parsing survey responses CSV:', error);
            }
        };

        // Call readFeaturesFile function
        readFeaturesFile();
        // Call readSurveyResponsesFile function
        readSurveyResponsesFile();
    }, []); // Empty dependency array ensures the effect runs only once when the component mounts

    const parseFeaturesCSV = (csvData) => {
        Papa.parse(csvData, {
            header: true,
            skipEmptyLines: true,
            complete: (result) => {
                const parsedData = result.data;
                const uniqueCategories = [...new Set(parsedData.map(item => item.Category))];
                setCategories(uniqueCategories);
                setFeatures(parsedData);
                setShowFileInput(false);
            },
            error: (error) => {
                console.error('Error parsing features CSV:', error);
            }
        });
    };

    const parseSurveyResponsesCSV = (csvData) => {
        Papa.parse(csvData, {
            header: true,
            skipEmptyLines: true,
            complete: (result) => {
                const parsedData = result.data;
                setSurveyResponses(parsedData);
            },
            error: (error) => {
                console.error('Error parsing survey responses CSV:', error);
            }
        });
    };

    const handleCategoryClick = (category) => {
        setSelectedCategory(category);
    };

    const handleFeatureButtonClick = (id) => {
        const response = surveyResponses.find(response => response.id === id);
        setSelectedFeature(response);
    };

    return (
        <div className="container">

            <div className="categories">
                {categories.map((category, index) => (
                    <button
                        key={index}
                        onClick={() => handleCategoryClick(category)}
                        className={index % 2 === 0 ? 'even-category' : 'odd-category'}
                    >
                        {category}
                    </button>
                ))}
            </div>
            <div className="features">
                <ul>
                    {selectedCategory &&
                        features
                            .filter(item => item.Category === selectedCategory)
                            .map((item, index) => (
                                <li key={index}>
                                    <span>{item.Features}</span>
                                    <button className={index % 2 === 0 ? 'even-button' : 'odd-button'} onClick={() => handleFeatureButtonClick(item.id)}>Read more</button>
                                </li>
                            ))}
                </ul>
            </div>
            <div className="user-hate-box">
                {selectedFeature && (
                    <div>
                        <h3>
                            {selectedFeature.user_name}
                            <span className="tabular-space"></span>
                            {selectedFeature.star_rating} out of 5
                        </h3>
                        <p style={{ marginBottom: '5px' }}>Published at: {new Date(selectedFeature.submitted_at).toISOString().split('T')[0]}</p>
                        <p>{selectedFeature.hate}</p>
                    </div>
                )}
            </div>
            <style jsx>{`
                .container {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    padding: 20px;
                }
                .categories {
                    margin-top: 20px;
                    display: flex;
                    justify-content: space-evenly; // evenly space the buttons
                    flex-wrap: wrap; // allow wrapping of buttons if necessary
                }
                .categories button {
                    margin: 5px;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                }
                .even-category {
                    background-color: #000;
                    color: #fff;
                }
                .odd-category {
                    background-color: orange;
                    color: #fff;
                }
                .features {
                    margin-top: 20px;
                    margin-left:-100px;
                }
                .features ul {
                    list-style-type: none;
                    padding: 0;
                }
                .features li {
                    margin-bottom: 10px;
                }
                .features li span {
                    margin-right: 10px; // Add space between feature text and button
                }
                .even-button, .odd-button {
                    border-radius: 5px; // Rounded button
                }
                .even-button {
                    background-color: #000;
                    color: #fff;
                }
                .odd-button {
                    background-color: orange;
                    color: #fff;
                }
                .user-hate-box {
                    position: absolute;
                    margin-top: 100px;
                    margin-left: 1000px;
                    margin-right:100px;
                    padding: 20px;
                    border-radius: 5px;
                }
                .user-hate-box h3 {
                    margin-bottom: 10px;
                }
                .user-hate-box p {
                    margin: 0;
                }
                .tabular-space {
                    display: inline-block;
                    width: 70px; /* Adjust the width as needed */
                }
            `}</style>
        </div>
    );
}

export default Feature;
