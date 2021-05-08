import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axiosMain from '../../http/axios/axios_main';
import { toast } from 'react-toastify';

import Sidebar from '../../components/Sidebar/Sidebar';
import Header from '../../components/Header/Header';
import Pdf from '../../assets/wof.pdf';

const BookShelf = props => {

    const [data, setData] = useState([]);
    const [errValue, setErrValue] = useState();

    useEffect(() => {
        getBooksOwned();
    }, []);

    const getBooksOwned = () => {
        const userId = localStorage.getItem('userId');
        axiosMain
            .get('/ownbookusr/' + "?pk=" + userId)
            .then(response => {
                if (response.status === 200) {
                    setData(response.data);
                    toast.success(`User Books Fetch Successful`, {
                        position: 'top-right',
                        autoClose: 3000,
                        hideProgressBar: true,
                        closeOnClick: true,
                        pauseOnHover: true,
                        draggable: true,
                        progress: undefined,
                    });
                }
            })
            .catch(error => {
                setErrValue(error);
                console.error('Error', error);
                setErrValue("This Books Fetch Failed")
            });
    };
    return (
        <React.Fragment>
            <Header />
            <Sidebar />
            <br />
            <br />
            <br />
            <br />
            <br />
            <div className="headingstyle">
                <h1>My Bookshelf</h1>
            </div>
            <div className="bookshelf">

                {data.length >= 1 && data.map(({ bookJSON }, index) => (
                    <>
                        {index % 2 == 0 ?
                            <div className="book book-blue" onClick={(e) => { }}>
                                <h2 color="black">{bookJSON.name}</h2>
                                <a href = {Pdf} target = "_blank"><span><i className="icofont-link"></i></span></a>
                            </div> :
                            <div className="book-tilted">
                                <div className="book book-umber">
                                    <h2 style={{ color: "white" }}>{bookJSON.name}</h2>
                                    <a href = {Pdf} target = "_blank"><span><i className="icofont-link"></i></span></a>
                                   
                                </div>
                            </div>
                        }
                    </>
                ))}

            </div>


        </React.Fragment >

    );
}

export default BookShelf;
