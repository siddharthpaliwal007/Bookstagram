import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axiosMain from '../../http/axios/axios_main';
import { toast } from 'react-toastify';
import Sidebar from '../../components/Sidebar/Sidebar';
import Header from '../../components/Header/Header';
import Tree from 'react-d3-tree';
import CustomDropdown from "../../components/CustomDropdown/CustomDropdown";


const ReferralTree = props => {
    const [data, setData] = useState({});
    const [errValue, setErrValue] = useState();
    const [chartData, setChartData] = useState({});
    const [selectOptions, setSelectionOptions] = useState([]);
    const [findId, setFindId] = useState([]);
    const [bookForTree, setBookForTree] = useState();

    useEffect(() => {

        getTree();
        getMyBookDropdown();

    }, [bookForTree]);

    const getTree = () => {
        if (bookForTree) {
            findId.map(({ name, id }, index) => {
                if (name == bookForTree) {
                    axiosMain
                        .get('/activate_Tree/' + "?pk=" + id)
                        .then(response => {
                            if (response.status === 200) {
                                let dataArr = [];
                                let idArr = [];
                                console.log("Response", response.data);

                                dataArr.push({
                                    name: response.data.name,
                                    attributes: response.data.attributes,
                                    children: response.data.children
                                });

                                setChartData(dataArr);
                            }
                        })
                        .catch((error) => {
                            console.error("Error", error);
                            setErrValue("The Crypto Data Feetch Unsuccessful");
                        });
                }
            })
        } else {
            axiosMain
                .get('/activate_Tree/' + "?pk=" + 7)
                .then(response => {
                    if (response.status === 200) {
                        let dataArr = [];
                        let idArr = [];
                        console.log("Response", response.data);

                        dataArr.push({
                            name: response.data.name,
                            attributes: response.data.attributes,
                            children: response.data.children
                        });

                        setChartData(dataArr);
                    }
                })
                .catch((error) => {
                    console.error("Error", error);
                    setErrValue("The Crypto Data Feetch Unsuccessful");
                });
        }
    };

    const getMyBookDropdown = () => {
        const userId = localStorage.getItem('userId');
        axiosMain
            .get('/book/')
            .then(response => {
                if (response.status === 200) {
                    let dataArr = [];
                    let idArr = [];
                    // data.length >= 1 && data.map(({ bookJSON }, index) => (

                    // ));
                    (response.data).map(({ id, name, authJSON }, index) => {

                        if(authJSON.id == userId)
                        { 
                        dataArr.push({
                            label: name,
                            value: name,
                        });
                        idArr.push({
                            id: id,
                            name: name,
                        });
                    }
                    });
                        
                    setSelectionOptions(dataArr);
                    setFindId(idArr);
                }
            })
            .catch((error) => {
                console.error("Error", error);
                setErrValue("The Crypto Data Feetch Unsuccessful");
            });
    };

    const handleDropdown  = async (selected) => {
        await setBookForTree(selected);
        // getTree();
    }
    return (
        <React.Fragment>
            <Header />
            <Sidebar />
            <br />
            <br />
            <br />
            <br />
            <div className="container">
                <CustomDropdown
                    className="form-select"
                    name="report-type"
                    id="report-select"
                    options={selectOptions}
                    onChangeOption={(selected) => { handleDropdown(selected) }}

                />

                {chartData ?
                    <div id="treeWrapper" style={{ width: '100em', height: '50em' }}>
                        <Tree data={chartData} />
                    </div> :
                    null
                }

            </div>

        </React.Fragment>
    )
};

export default ReferralTree;
