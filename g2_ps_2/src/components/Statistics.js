import React, { useState } from 'react';
import Rating from '@mui/material/Rating';

const Statistics = ({ data }) => {
    const [selectedReviewIndex, setSelectedReviewIndex] = useState(null);
    const [searchKeyword, setSearchKeyword] = useState('');

    const countStarRatings = (rating) => {
        const flooredRating = Math.floor(parseFloat(rating));
        return data.filter(review => Math.floor(parseFloat(review.star_rating)) === flooredRating).length;
    };

    const ratingItems = [
        { value: 5, label: 'Five Star' },
        { value: 4, label: 'Four Stars' },
        { value: 3, label: 'Three Stars' },
        { value: 2, label: 'Two Stars' },
        { value: 1, label: 'One Star' }
    ];

    const totalReviews = data.length;

    // Calculate the average rating
    const averageRating = data.reduce((sum, review) => sum + parseFloat(review.star_rating), 0) / totalReviews;

    // Top 5 words from the CSV file
    const topLoveKeywords = ["great", "good", "helpful", "easy", "responsive"];
    const topHateKeywords = ["unbiased", "low", "costly", "hard", "negative"];

    // Function to find the index of the first review containing the selected adjective or search keyword
    const findReviewIndex = (keyword) => {
        return data.findIndex(review => review.love.toLowerCase().includes(keyword.toLowerCase()) || review.hate.toLowerCase().includes(keyword.toLowerCase()));
    };

    // Handle button click to find and store the index of the review containing the selected keyword
    const handleButtonClick = (keyword) => {
        const index = findReviewIndex(keyword);
        setSelectedReviewIndex(index);
    };

    // Handle search input change
    const handleSearchInputChange = (event) => {
        setSearchKeyword(event.target.value);
    };

    // Handle search button click
    const handleSearchButtonClick = () => {
        const index = findReviewIndex(searchKeyword);
        setSelectedReviewIndex(index);
    };

    return (
        <div style={{ width: '900px', height: '400px', borderRadius: '10px', border: '1px solid #ccc', padding: '20px', marginLeft: '500px' }}>
            <div style={{ display: 'flex' }}>
                <div style={{ width: '450px', height: '250px', borderRadius: '10px', padding: '10px', fontFamily: 'Arial, sans-serif' }}>
                    <p style={{ fontSize: '18px', fontWeight: 'bold', marginBottom: '0px', marginLeft: '-270px' }}>{totalReviews} Total Reviews</p>
                    <div style={{ display: 'flex', alignItems: 'center', marginBottom: '10px', marginLeft: '-15px' }}>
                        <Rating name="average-rating" value={averageRating} precision={0.5} readOnly />
                        <span style={{ marginLeft: '8px' }}>{averageRating.toFixed(1)} out of 5 </span>
                    </div>
                    {ratingItems.map(item => (
                        <div key={item.value} style={{ marginBottom: '-15px', display: 'flex', alignItems: 'center' }}>
                            <p> {item.value} stars</p>
                            <div style={{ marginLeft: '10px', width: '300px', height: '20px', backgroundColor: 'grey', borderRadius: '10px', border: '1px solid #FFD700' }}>
                                <div style={{ width: `${(countStarRatings(item.value) / totalReviews) * 100}%`, height: '100%', backgroundColor: 'orange', borderRadius: '10px' }}></div>
                            </div>
                            <span style={{ marginLeft: '5px', fontSize: '14px' }}>{countStarRatings(item.value)} </span>
                        </div>
                    ))}
                </div>
                <div style={{ marginTop: '25px', display: 'flex', flexDirection: 'column', marginLeft: '10px', alignItems: 'center' }}>
                    <div style={{ position: 'relative', width: '376px', height: '30px', borderRadius: '15px', marginBottom: '30px' }}>
                        <input type="text" placeholder="Search reviews..." value={searchKeyword} onChange={handleSearchInputChange} style={{ width: '100%', height: '100%', borderRadius: '15px', paddingLeft: '35px', border: '1px solid black' }} />
                        <button onClick={handleSearchButtonClick} style={{ position: 'absolute', top: '55%', right: '-10px', transform: 'translateY(-50%)', border: 'none', backgroundColor: '#FFD700', padding: '5px 10px', borderRadius: '5px', cursor: 'pointer' }}>Search</button>
                    </div>
                    <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', marginLeft: '-20px' }}>
                        {topLoveKeywords.map((keyword, index) => (
                            <button key={index} onClick={() => handleButtonClick(keyword)} style={{ borderRadius: '20px', padding: '5px 15px', backgroundColor: '#FFD700', border: 'none', cursor: 'pointer', marginBottom: '10px', marginRight: '5px', color: 'black' }}>{keyword}</button>
                        ))}
                    </div>
                    <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', marginLeft: '3px' }}>
                        {topHateKeywords.map((keyword, index) => (
                            <button key={index} onClick={() => handleButtonClick(keyword)} style={{ borderRadius: '20px', padding: '5px 15px', backgroundColor: '#FFD700', border: 'none', cursor: 'pointer', marginBottom: '10px', marginRight: '3px', color: 'black' }}>{keyword}</button>
                        ))}
                    </div>
                    {/* Display filtered review if a keyword is selected */}
                    {selectedReviewIndex !== null && data[selectedReviewIndex] ? (
                        <div style={{ marginTop: '20px' }}>
                            <div style={{ width: '98%', marginBottom: '10px', minHeight: '95px', border: '1px solid black', borderRadius: '10px', padding: '10px', display: 'flex', flexDirection: 'column' }}>
                                <p style={{ display: 'flex', justifyContent: 'space-between' }}>
                                    <span style={{ fontSize: '16px', fontWeight: 'bold' }}>{data[selectedReviewIndex].user_name}</span>
                                    <span style={{ fontSize: '14px', fontWeight: 'bold' }}> "{data[selectedReviewIndex].title}"</span>
                                </p>
                                <p style={{ fontSize: '10px', marginTop: '-5px' }}>{data[selectedReviewIndex].love}</p>
                                <p style={{ fontSize: '10px', marginTop: '-5px' }}>{data[selectedReviewIndex].hate}</p>
                            </div>
                        </div>
                    ) : (
                        searchKeyword && <p>No reviews found with the given keyword.</p>
                    )}

                </div>
            </div>


        </div>
    );
}

export default Statistics;
