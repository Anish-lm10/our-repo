import React, { useEffect, useState } from "react";
import axios from "axios";
import Navbar from "./Navbar";

const JobSearch = () => {
  const [myData, setMyData] = useState([]);

  useEffect(() => {

    // axios.get("https://dummyjson.com/users").then((res) => {
    //   setMyData(res.data.users);
    //   console.log(res.data.users);
    // });

    axios.get("").then((res) => {
      setMyData(res.data);
      console.log(res.data);
    });
    
  }, []);

  return (
    <div className="bg-[#0F172A] flex flex-col items-center justify-center box-border">
      <Navbar />
      <form>
        <div className=" p-4 grid grid-cols-4 gap-4">
          <select className="bg-white border-[#0F172A] border-2 text-[#0F172A] py-2 px-4 rounded outline-none">
            <option value="part-time">Part-time</option>
            <option value="full-time">Full-time</option>
            <option value="freelance">Freelance</option>
          </select>
          <input
            type="text"
            id="location"
            name="location"
            className="bg-white border-[#0F172A] border-2 text-[#0F172A] py-2 px-4 rounded outline-none"
            placeholder="enter location"
            required
          />
          <input
            type="text"
            id="skill"
            name="skill"
            className="bg-white border-[#0F172A] border-2 text-[#0F172A] py-2 px-4 rounded outline-none"
            placeholder="enter skills"
            required
          />
          <button
            className="text-lg rounded bg-blue-200 border-none py-1 px-4 text-[#0F172A] font-semibold"
          >
            search
          </button>
        </div>
      </form>
      <div className="bg-white w-[80%] grid grid-cols-2 gap-5 p-[30px] ">
        {myData.map((post) => {
          const { companyname, jobname, experience, skills,salary,location, id } = post;
          return (
            <div key={id} className="container flex w-[80%] justify-evenly">
              <div className="bg-white rounded-md border border-2 border-black w-full h-[40hv] p-3 text-white ">
                <div className="px-[20px] rounded bg-[#0F172A] h-[35vh] flex flex-col justify-center gap-[20px] ">
                  <div className="flex ">
                    <div className="text-lg">companyname</div>
                  </div>
                  <div className="text-5xl font-bold">jobname</div>
                  <div className="flex flex-wrap gap-[10px]">
                    <button className="border bg-transparent text-white rounded h-[30px] text-sm flex justify-center items-center">
                     Project work
                    </button>
                    <button className="border bg-transparent text-white rounded h-[30px] text-sm flex justify-center items-center">
                      experience
                    </button>
                    <button className="border bg-transparent text-white rounded h-[30px] text-sm flex justify-center items-center">
                    skills 
                    </button>
                    {/* <button className="border bg-transparent text-white rounded h-[30px] text-sm">skills</button> */}
                  </div>
                </div>
                <div className="flex pt-4 justify-between items-center ">
                  <div className="text-[#0F172A] px-[20px] font-semibold ">
                    <div className="font-bold italic	">salary</div>
                    <div>location</div>
                  </div>
                  <button
            className=" text-lg rounded bg-[#0F172A] border-none py-1 px-4 text-white "
          >
            Details
          </button>
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default JobSearch;
