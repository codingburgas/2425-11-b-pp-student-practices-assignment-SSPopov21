import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { X } from "lucide-react";

const SkillsForm = () => {
  const navigate = useNavigate();
  const [currentSkill, setCurrentSkill] = useState("");
  const [skills, setSkills] = useState<string[]>([]);

  const handleAddSkill = (e: React.FormEvent) => {
    e.preventDefault();
    if (currentSkill.trim() && !skills.includes(currentSkill.trim())) {
      setSkills([...skills, currentSkill.trim()]);
      setCurrentSkill("");
    }
  };

  const handleRemoveSkill = (skillToRemove: string) => {
    setSkills(skills.filter(skill => skill !== skillToRemove));
  };

  const handleSubmit = () => {
    if (skills.length > 0) {
      navigate('/predictions', { state: { skills } });
    }
  };

  return (
    <Card className="w-full max-w-2xl mx-auto">
      <CardHeader>
        <CardTitle>Enter Your Skills</CardTitle>
      </CardHeader>
      <CardContent>
        <form onSubmit={handleAddSkill} className="space-y-4">
          <div className="flex gap-2">
            <Input
              type="text"
              value={currentSkill}
              onChange={(e) => setCurrentSkill(e.target.value)}
              placeholder="Enter a skill (e.g., React, Python, TypeScript)"
              className="flex-1"
            />
            <Button type="submit">Add Skill</Button>
          </div>
        </form>

        <div className="mt-4">
          <div className="flex flex-wrap gap-2">
            {skills.map((skill, index) => (
              <Badge key={index} variant="secondary" className="flex items-center gap-1">
                {skill}
                <button
                  onClick={() => handleRemoveSkill(skill)}
                  className="ml-1 hover:text-destructive"
                >
                  <X className="h-3 w-3" />
                </button>
              </Badge>
            ))}
          </div>
        </div>

        <div className="mt-6">
          <Button
            onClick={handleSubmit}
            disabled={skills.length === 0}
            className="w-full"
          >
            Get Prediction
          </Button>
        </div>
      </CardContent>
    </Card>
  );
};

export default SkillsForm; 