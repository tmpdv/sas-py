import React from "react";
import PropTypes from "prop-types";
import SwipeableViews from "react-swipeable-views";
import { makeStyles } from "@material-ui/core/styles";
import AppBar from "@material-ui/core/AppBar";
import Tabs from "@material-ui/core/Tabs";
import Tab from "@material-ui/core/Tab";
import Box from "@material-ui/core/Box";

const TabPanel = (props) => {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`full-width-tabpanel-${index}`}
      aria-labelledby={`full-width-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Box
          p={3}
          display="flex"
          flexDirection="column"
          justifyContent="center"
          alignItems="center"
        >
          {children}
        </Box>
      )}
    </div>
  );
}

TabPanel.propTypes = {
  children: PropTypes.node,
  index: PropTypes.any.isRequired,
  value: PropTypes.any.isRequired,
};

function a11yProps(index) {
  return {
    id: `full-width-tab-${index}`,
    "aria-controls": `full-width-tabpanel-${index}`,
  };
}

const useStyles = makeStyles((theme) => ({
  root: {
    backgroundColor: theme.palette.background.paper,
    width: "100%",
  },
  audio: {
    outline: "none",
    marginBottom: "1em",
  },
  image: {
    marginBottom: "1em",
    width: "15em"
  },
}));


export default function FullWidthTabs({tracks, images, about}) {
  const classes = useStyles();
  const theme = useStyles();
  const [value, setValue] = React.useState(0);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  const handleChangeIndex = (index) => {
    setValue(index);
  };

  return (
    <div className={classes.root}>
      <AppBar position="static" color="default">
        <Tabs
          value={value}
          onChange={handleChange}
          indicatorColor="primary"
          textColor="primary"
          variant="fullWidth"
          aria-label="full width tabs example"
        >
          <Tab label="Tracks" {...a11yProps(0)} />
          <Tab label="Visuals" {...a11yProps(1)} />
          <Tab label="About" {...a11yProps(2)} />
        </Tabs>
      </AppBar>
      <SwipeableViews
        axis={theme.direction === "rtl" ? "x-reverse" : "x"}
        index={value}
        onChangeIndex={handleChangeIndex}
      >
        <TabPanel value={value} index={0} dir={theme.direction}>
            {tracks && tracks.map((track) => (
              <React.Fragment>
                  <p>{track.name}</p>
                  <audio controls src={track.link} key={track.link} className={classes.audio}/>
              </React.Fragment>
            ))}
        </TabPanel>
        <TabPanel value={value} index={1} dir={theme.direction}>
            {images && images.map((image) => (
              <img src={image.link} key={image.id} alt="" className={classes.image} />
            ))}
        </TabPanel>
        <TabPanel value={value} index={2} dir={theme.direction}>
            <p>{about && about.value}</p>
        </TabPanel>
      </SwipeableViews>
    </div>
  );
}
