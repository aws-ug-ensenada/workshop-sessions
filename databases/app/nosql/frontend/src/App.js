import React, { useState, useEffect } from "react";

const App = () => {
    const [users, setUsers] = useState([]); // Ensure it's always an array
    const [name, setName] = useState("");
    const [age, setAge] = useState("");
    const [career, setCareer] = useState({ title: "", industry: "", experience_years: "" });
    const [skills, setSkills] = useState("[]"); // JSON format
    const [hobbies, setHobbies] = useState("");

    // Fetch users from backend
    useEffect(() => {
        fetch("http://localhost:5000/get_users")
            .then(response => response.json())
            .then(data => {
                console.log("Fetched users:", data);
                setUsers(Array.isArray(data) ? data : []); // Ensure it's an array
            })
            .catch(error => console.error("Error fetching users:", error));
    }, []);

    // Add user
    const addUser = () => {
        const parsedSkills = JSON.parse(skills || "[]"); // Parse JSON safely
        const formattedHobbies = hobbies.split(",").map(h => h.trim()); // Convert to array

        const newUser = {
            name,
            age: Number(age),
            career,
            skills: parsedSkills,
            hobbies: formattedHobbies
        };

        fetch("http://localhost:5000/add_user", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(newUser),
        })
            .then(response => response.json())
            .then(data => {
                console.log("User added:", data);
                setUsers(prevUsers => [...prevUsers, newUser]); // Add to local state
                setName(""); setAge(""); setCareer({ title: "", industry: "", experience_years: "" });
                setSkills("[]"); setHobbies("");
            })
            .catch(error => console.error("Error adding user:", error));
    };

    // Delete user
    const deleteUser = async (userId) => {
      try {
          await fetch(`http://localhost:5000/delete_user/${userId}`, { method: "DELETE" });
          setUsers(users.filter(user => user.user_id !== userId)); // Update UI
      } catch (error) {
          console.error("Error deleting user:", error);
      }
    };
  

    return (
        <div style={{ padding: "20px" }}>
            <h1>DynamoDB Users</h1>
            
            {/* User Input Form */}
            <input type="text" placeholder="Name" value={name} onChange={(e) => setName(e.target.value)} />
            <input type="number" placeholder="Age" value={age} onChange={(e) => setAge(e.target.value)} />

            <h2>Career</h2>
            <input type="text" placeholder="Title" value={career.title} onChange={(e) => setCareer({ ...career, title: e.target.value })} />
            <input type="text" placeholder="Industry" value={career.industry} onChange={(e) => setCareer({ ...career, industry: e.target.value })} />
            <input type="number" placeholder="Years of Experience" value={career.experience_years} onChange={(e) => setCareer({ ...career, experience_years: e.target.value })} />

            <h3>Skills (JSON format: {"[{\"skill\": \"Python\", \"level\": \"Advanced\"}]"})</h3>
            <input type="text" placeholder='[{"skill": "Python", "level": "Advanced"}]' value={skills} onChange={(e) => setSkills(e.target.value)} />

            <h3>Hobbies (Comma-separated)</h3>
            <input type="text" placeholder="Gaming, Reading, Hiking" value={hobbies} onChange={(e) => setHobbies(e.target.value)} />

            <button onClick={addUser}>Add User</button>

            <h2>Users</h2>

            {Array.isArray(users) ? users.map((user) => (
                <div key={user.user_id} style={{ border: "1px solid black", padding: "10px", margin: "10px" }}>
                    <h3>{user.name}</h3>
                    <p>Age: {user.age}</p>
                    <p>Career: {user.career?.title} in {user.career?.industry}</p>
            
                    <p><strong>Skills:</strong></p>
                    <ul>
                        {Array.isArray(user.skills) ? user.skills.map((skill, index) => (
                            <li key={index}>{skill.skill} - {skill.level}</li>
                        )) : <li>No skills listed</li>}
                    </ul>
            
                    <p><strong>Hobbies:</strong> {Array.isArray(user.hobbies) ? user.hobbies.join(", ") : "None"}</p>
            
                    <button 
                        onClick={() => deleteUser(user.user_id)} 
                        style={{ backgroundColor: "red", color: "white", border: "none", padding: "5px" }}
                    >
                        Delete
                    </button>
                </div>
            )) : <p>Loading users...</p>}



        </div>
    );
};

export default App;
