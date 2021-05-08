import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axiosMain from '../../http/axios/axios_main';
import { toast } from 'react-toastify';
import Sidebar from '../../components/Sidebar/Sidebar';
import Header from '../../components/Header/Header';

const BookGallery = props => {
    const [data, setData] = useState({});
    const [errValue, setErrValue] = useState();

    return (
        <React.Fragment>
            <Header />
            <Sidebar />
            <br />
            <br />
            <br />
            <br />

            {/* <button
                type='submit'
                className='btn btn-primary btn-block'
                onClick={() => handleSubmit()}
            >
                Create account
            </button> */}


        </React.Fragment>
    )
};

export default BookGallery;
