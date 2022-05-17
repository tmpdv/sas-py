import React, { useEffect, useState } from "react";
import { makeStyles, ThemeProvider } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardActionArea from "@material-ui/core/CardActionArea";
import CardContent from "@material-ui/core/CardContent";
import Typography from "@material-ui/core/Typography";
import Container from "@material-ui/core/Container";
import Grid from "@material-ui/core/Grid";
import { createMuiTheme } from "@material-ui/core/styles";
import grey from "@material-ui/core/colors/grey";

import TabPanel from "./TabPanel";


const useStyles = makeStyles({
    main: {
      background: `url(https://docs.google.com/uc?export=download&id=1_rsIQL5vscxsNAItQ3c4FTRvInz0dQf_)`,
      backgroundAttachment: "fixed",
      backgroundPosition: "center",
      backgroundSize: "cover",
    },
    card: {
      opacity: 0.8,
      minHeight: "100vh"
    }
  });

const MainPage = () => {
    const theme = createMuiTheme({
        palette: {
          type: "dark",
            primary: {
              main: grey[100],
            },
        },
      });

    const [tracks, setTracks] = useState();
        useEffect(() => {
            fetch("/data/tracks")
            .then(response => response.json())
            .then(tracks => setTracks(tracks))
            // .then(page => setTracks(page.elementList))
        }, []);

  const [images, setImages] = useState();
  useEffect(() => {
    fetch("/data/pictures")
      .then(response => response.json())
      .then(page => setImages(page.elementList))
  }, []);

  const [about, setAbout] = useState();
  useEffect(() => {
    fetch("/data/about")
    .then(response => response.json())
    .then(text => setAbout(text))
  }, []);

  const classes = useStyles();

  return (
    <ThemeProvider theme={theme}>
      <div className={classes.main}>
        <Container maxWidth="sm">
          <Card className={classes.card}>
            <CardActionArea>
              <CardContent>
                <Grid
                  container
                  direction="column"
                  justify="center"
                  alignItems="center"
                >
                  <Typography gutterBottom variant="h5" component="h2">
                    Staffs and Scrolls
                  </Typography>
                  <Typography
                    variant="body2"
                    color="textSecondary"
                    component="p"
                  >
                    Ambient. Visuals. Trips.
                  </Typography>
                </Grid>
              </CardContent>
            </CardActionArea>
            <TabPanel tracks={tracks} images={images} about = {about} />
          </Card>
        </Container>
      </div>
    </ThemeProvider>
    )
}

export default MainPage;
