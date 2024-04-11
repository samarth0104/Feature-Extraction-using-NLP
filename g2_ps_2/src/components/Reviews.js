import React from 'react';
import Stack from '@mui/material/Stack'; // Import Stack from MUI
import Rating from '@mui/material/Rating'; // Import Rating from MUI
import anonImage from 'C:/Users/samar/OneDrive/Desktop/PESU/Extra/G2/g2_ps_2/src/images/anon.jpg'; // Import your anonymous image

function Reviews({ chunkedData }) {
    return (
        <>
            {chunkedData.map((chunk, index) => (
                <div key={index} className="review-row" style={{ display: 'flex', justifyContent: 'space-evenly', marginLeft: '3px' }}>
                    {chunk.map((row, rowIndex) => (
                        <div key={rowIndex} style={{ width: '400px', marginBottom: '10px', minHeight: '200px', border: '1px solid black', borderRadius: '10px', padding: '10px', display: 'flex', flexDirection: 'column', marginRight: 'px' }}>
                            <div style={{ display: 'flex', justifyContent: 'space-evenly', alignItems: 'center', marginBottom: '10px' }}>
                                <div style={{ display: 'flex', alignItems: 'center' }}>
                                    <img
                                        src={getImageUrl(row.user_image_url)}
                                        alt={row.user_name}
                                        style={{ width: '50px', height: '50px', borderRadius: '50%', marginRight: '10px' }}
                                    />
                                    <div>
                                        <p style={{ fontSize: '20px', fontWeight: 'bold', textAlign: 'left' }}>
                                            {row.user_name}
                                            {row.verified_current_user === 'TRUE' && <span style={{ marginLeft: '5px' }}>&#10003;</span>}
                                        </p>
                                        <Stack direction="row" spacing={1} alignItems="center">
                                            <Rating name="half-rating" value={parseFloat(row.star_rating)} precision={0.5} readOnly />
                                            <span>{`${row.star_rating}/5.0`}</span>
                                        </Stack>
                                    </div>
                                </div>
                                <p style={{ fontSize: '12px', textAlign: 'right' }}>{row.submitted_at ? row.submitted_at.substring(0, 10) : ''}</p>
                            </div>
                            <div>
                                <p style={{ fontSize: '15px', fontWeight: 'bold', textAlign: 'left' }}>"{row.title}"</p>
                                <p style={{ fontSize: '12px', textAlign: 'left' }}>{row.love}</p>
                                <p style={{ fontSize: '12px', textAlign: 'left' }}>{row.hate}</p>
                            </div>
                        </div>
                    ))}
                </div>
            ))}
        </>
    );
}

function getImageUrl(url) {
    if (!url || !(url.endsWith('.jpg') || url.endsWith('.jpeg'))) {
        return anonImage;
    }
    return url;
}

export default Reviews;
