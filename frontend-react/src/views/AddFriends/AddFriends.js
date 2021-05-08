import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axiosMain from '../../http/axios/axios_main';
import { toast } from 'react-toastify';
import { Row, Col, Container } from "reactstrap";
// import "bootstrap/dist/css/bootstrap.css";
// import "font-awesome/css/font-awesome.min.css";
import { withRouter } from 'react-router';

import Sidebar from '../../components/Sidebar/Sidebar';
import Header from '../../components/Header/Header';


const AddFriends = props => {

    const [data, setData] = useState([]);
    const [addfriend, setAddFriend] = useState([]);

    const [errValue, setErrValue] = useState();

    useEffect(() => {
        console.log("From:", props);
        getSearchFriendList();
    }, [addfriend]);

    const getSearchFriendList = () => {
        const userId = localStorage.getItem('userId');
        axiosMain
            .get('/allfriend/' + '?pk=' + userId)
            .then(response => {
                if (response.status === 200) {
                    console.log("RESPONSE", response.data)
                    setData(response.data);
                    toast.success(`User Profile Fetch Successful`, {
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
                setErrValue("This User Profile Fetch Failed")
            });
    };

    const addFriendHandler = (friendId) => {
        const userId = localStorage.getItem('userId');

        axiosMain
            .post('/friend/', {
                user: userId,
                friend: friendId,
                relationship: "addfriend"
            })
            .then(response => {
                if (response.status === 200) {
                    console.log("RESPONSE", response.data);
                    setAddFriend(response.data);
                    toast.success(`User Profile Fetch Successful`, {
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
                setErrValue("This User Profile Fetch Failed")
            });
    }


    const handleInput = (val) => {
        console.log("Value", val)

            const filteredData = data.filter(element => {
                console.log("Element", element)

              return element.first_name.toLowerCase().includes(val.toLowerCase());
            });
            console.log("Filtered Data", filteredData)
            setData(filteredData);
          
    }
    return (
        <React.Fragment>
            <Header />
            <Sidebar />
            <br />
            <br />
            <br />
            <br />
            <br />

            <Container>
                <div className="row">
                    <div className="col-md-8">
                        <div className="people-nearby">
                        <div>Search</div>
                        <input type="text" id="Search" onChange={(e) => handleInput(e.target.value)} placeholder="Search Friends.." title="Type in a name"/>
                            {data.length >= 1 && data.map(({ id, dp, username, first_name, usertype, country }, index) => (
                                < div className="nearby-user" >
                                    <div className="row">
                                        <div className="col-md-2 col-sm-2">
                                            <img src={dp} alt="user" className="profile-photo-lg" />
                                        </div>
                                        <div className="col-md-7 col-sm-7">
                                            <h5><a href="#" className="profile-link">{username}</a></h5>
                                            <p>{usertype}</p>
                                            <p className="text-muted">{country}</p>
                                        </div>
                                        <div className="col-md-3 col-sm-3">
                                            <button
                                                className="btn btn-primary pull-right"
                                                onClick={(e) => { addFriendHandler(id) }}
                                            >
                                                Add Friend
                                            </button>

                                        </div>
                                    </div>
                                </div>
                            ))}

                        </div>
                    </div>
                </div>

            </Container >

        </React.Fragment >

    );
}
export default withRouter(AddFriends);

