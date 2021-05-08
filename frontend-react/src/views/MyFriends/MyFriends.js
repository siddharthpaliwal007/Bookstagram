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
    const [pendingData, setPendingData] = useState([]);
    const [friends, setFriends] = useState([]);
    const [unfriend, setUnfriend] = useState([]);

    const [errValue, setErrValue] = useState();
    const [searchFriend, setSearchFriend] = useState();

    useEffect(() => {
        getFriendList();
        getPendingList();
    }, [friends] || unfriend);

    const getFriendList = () => {
        const userId = localStorage.getItem('userId');
        axiosMain
            .get('/friendlist/' + userId + '/')
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

    const getPendingList = () => {
        const userId = localStorage.getItem('userId');
        axiosMain
            .get('/acceptfriend/' + userId + '/')
            .then(response => {
                if (response.status === 200) {
                    console.log("RESPONSE", response.data);

                    setPendingData(response.data);

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

    const removeFriendHandler = (friendId) => {
        const userId = localStorage.getItem('userId');

        axiosMain
            .get('/unfriend/?pk=' + userId + '&friend=' + friendId)
            .then(response => {
                if (response.status === 200) {
                    console.log("RESPONSE", response.data);
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
                window.location.reload(false);

            })
            .catch(error => {
                setErrValue(error);
                console.error('Error', error);
                setErrValue("This User Profile Fetch Failed")
            });
    }

    const acceptFriendHandler = (friendId) => {
        const userId = localStorage.getItem('userId');

        axiosMain
            .put('/friendupdate/', {
                user: userId,
                friend: friendId,
                relationship: "friends"
            })
            .then(response => {
                if (response.status === 200) {
                    console.log("RESPONSE", response.data);
                    setFriends(response.data);

                    toast.success(`User Profile Fetch Successful`, {
                        position: 'top-right',
                        autoClose: 3000,
                        hideProgressBar: true,
                        closeOnClick: true,
                        pauseOnHover: true,
                        draggable: true,
                        progress: undefined,
                    });
                    window.location.reload(false);

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
                            
                            {data.length >= 1 && data.map(({ id, dp, first_name, username, last_name, usertype, country }, index) => (
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
                                                onClick={(e) => { removeFriendHandler(id) }}
                                            >
                                                Remove Friend
                                            </button>

                                        </div>
                                    </div>
                                </div>
                            ))}

                            {pendingData.length >= 1 && pendingData.map(({ id, username, first_name, last_name, usertype, country }, index) => (
                                < div className="nearby-user" >
                                    <div className="row">
                                        <div className="col-md-2 col-sm-2">
                                            <img src='https://bootdey.com/img/Content/avatar/avatar7.png' alt="user" className="profile-photo-lg" />
                                        </div>
                                        <div className="col-md-7 col-sm-7">
                                            <h5><a href="#" className="profile-link">{username}</a></h5>
                                            <p>{usertype}</p>
                                            <p className="text-muted">{country}</p>
                                        </div>
                                        <div className="col-md-3 col-sm-3">
                                            <button
                                                className="btn btn-primary pull-right"
                                                onClick={(e) => { acceptFriendHandler(id) }}
                                            >
                                                Accept Request
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

