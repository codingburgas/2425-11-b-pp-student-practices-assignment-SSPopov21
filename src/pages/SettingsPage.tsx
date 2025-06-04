
import { useState } from "react";
import Header from "@/components/Header";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Switch } from "@/components/ui/switch";
import { Textarea } from "@/components/ui/textarea";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { toast } from "sonner";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";

const SettingsPage = () => {
  const [saving, setSaving] = useState(false);
  
  // Mock profile data
  const [profile, setProfile] = useState({
    name: "Alex Johnson",
    email: "alex@example.com",
    title: "Frontend Developer",
    skills: "React, TypeScript, Node.js",
    experience: "3 years",
    education: "Bachelor's in Computer Science",
    resumeUrl: "",
    portfolioUrl: "https://portfolio.example.com",
    linkedinUrl: "https://linkedin.com/in/alexjohnson",
    githubUrl: "https://github.com/alexjohnson",
  });

  const [preferences, setPreferences] = useState({
    emailNotifications: true,
    applicationReminders: true,
    weeklyReports: true,
    theme: "light",
    followUpReminders: true,
    interviewPrep: true,
  });

  const handleProfileChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setProfile({
      ...profile,
      [name]: value,
    });
  };

  const handlePreferenceChange = (name: string, value: boolean | string) => {
    setPreferences({
      ...preferences,
      [name]: value,
    });
  };

  const saveChanges = async () => {
    setSaving(true);
    
    // Simulate API call
    try {
      // In a real app, this would be an API call
      await new Promise(resolve => setTimeout(resolve, 1000));
      
      toast.success("Settings saved successfully!");
    } catch (error) {
      toast.error("Failed to save settings. Please try again.");
    } finally {
      setSaving(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <Header />
      <main className="container mx-auto px-4 py-8">
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">Settings</h1>
          <p className="text-gray-600">
            Customize your job application tracking experience and update your profile
          </p>
        </div>
        
        <div className="max-w-4xl mx-auto">
          <Tabs defaultValue="profile">
            <TabsList className="mb-8 grid grid-cols-2 w-[400px]">
              <TabsTrigger value="profile">Profile</TabsTrigger>
              <TabsTrigger value="preferences">Preferences</TabsTrigger>
            </TabsList>
            
            <TabsContent value="profile">
              <Card className="shadow-md">
                <CardHeader>
                  <CardTitle>Your Profile</CardTitle>
                  <CardDescription>
                    This information will be used for job application tracking and analysis
                  </CardDescription>
                </CardHeader>
                <CardContent className="space-y-6">
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div className="space-y-2">
                      <Label htmlFor="name">Full Name</Label>
                      <Input 
                        id="name" 
                        name="name" 
                        value={profile.name} 
                        onChange={handleProfileChange} 
                      />
                    </div>
                    
                    <div className="space-y-2">
                      <Label htmlFor="email">Email</Label>
                      <Input 
                        id="email" 
                        name="email" 
                        type="email" 
                        value={profile.email} 
                        onChange={handleProfileChange} 
                      />
                    </div>
                    
                    <div className="space-y-2">
                      <Label htmlFor="title">Job Title</Label>
                      <Input 
                        id="title" 
                        name="title" 
                        value={profile.title} 
                        onChange={handleProfileChange} 
                      />
                    </div>
                    
                    <div className="space-y-2">
                      <Label htmlFor="experience">Experience</Label>
                      <Input 
                        id="experience" 
                        name="experience" 
                        value={profile.experience} 
                        onChange={handleProfileChange} 
                      />
                    </div>
                    
                    <div className="space-y-2">
                      <Label htmlFor="education">Education</Label>
                      <Input 
                        id="education" 
                        name="education" 
                        value={profile.education} 
                        onChange={handleProfileChange} 
                      />
                    </div>
                    
                    <div className="space-y-2">
                      <Label htmlFor="resumeUrl">Resume URL</Label>
                      <Input 
                        id="resumeUrl" 
                        name="resumeUrl" 
                        value={profile.resumeUrl} 
                        onChange={handleProfileChange} 
                        placeholder="Link to your resume"
                      />
                    </div>
                  </div>
                  
                  <div className="space-y-2">
                    <Label htmlFor="skills">Skills</Label>
                    <Textarea 
                      id="skills" 
                      name="skills" 
                      value={profile.skills} 
                      onChange={handleProfileChange} 
                      placeholder="List your key skills"
                    />
                  </div>
                  
                  <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <div className="space-y-2">
                      <Label htmlFor="portfolioUrl">Portfolio URL</Label>
                      <Input 
                        id="portfolioUrl" 
                        name="portfolioUrl" 
                        value={profile.portfolioUrl} 
                        onChange={handleProfileChange} 
                      />
                    </div>
                    
                    <div className="space-y-2">
                      <Label htmlFor="linkedinUrl">LinkedIn URL</Label>
                      <Input 
                        id="linkedinUrl" 
                        name="linkedinUrl" 
                        value={profile.linkedinUrl} 
                        onChange={handleProfileChange} 
                      />
                    </div>
                    
                    <div className="space-y-2">
                      <Label htmlFor="githubUrl">GitHub URL</Label>
                      <Input 
                        id="githubUrl" 
                        name="githubUrl" 
                        value={profile.githubUrl} 
                        onChange={handleProfileChange} 
                      />
                    </div>
                  </div>
                </CardContent>
                <CardFooter className="flex justify-end">
                  <Button onClick={saveChanges} disabled={saving}>
                    {saving ? "Saving..." : "Save Changes"}
                  </Button>
                </CardFooter>
              </Card>
            </TabsContent>
            
            <TabsContent value="preferences">
              <Card className="shadow-md">
                <CardHeader>
                  <CardTitle>Preferences</CardTitle>
                  <CardDescription>
                    Customize notifications and application settings
                  </CardDescription>
                </CardHeader>
                <CardContent className="space-y-6">
                  <div className="space-y-6">
                    <div className="flex items-center justify-between">
                      <div>
                        <h3 className="font-medium">Email Notifications</h3>
                        <p className="text-sm text-gray-500">
                          Receive updates about your job applications via email
                        </p>
                      </div>
                      <Switch 
                        checked={preferences.emailNotifications} 
                        onCheckedChange={(checked) => 
                          handlePreferenceChange("emailNotifications", checked)
                        }
                      />
                    </div>
                    
                    <div className="flex items-center justify-between">
                      <div>
                        <h3 className="font-medium">Application Reminders</h3>
                        <p className="text-sm text-gray-500">
                          Get reminders about pending applications
                        </p>
                      </div>
                      <Switch 
                        checked={preferences.applicationReminders} 
                        onCheckedChange={(checked) => 
                          handlePreferenceChange("applicationReminders", checked)
                        }
                      />
                    </div>
                    
                    <div className="flex items-center justify-between">
                      <div>
                        <h3 className="font-medium">Weekly Reports</h3>
                        <p className="text-sm text-gray-500">
                          Receive weekly summary of your application progress
                        </p>
                      </div>
                      <Switch 
                        checked={preferences.weeklyReports} 
                        onCheckedChange={(checked) => 
                          handlePreferenceChange("weeklyReports", checked)
                        }
                      />
                    </div>
                    
                    <div className="flex items-center justify-between">
                      <div>
                        <h3 className="font-medium">Follow-up Reminders</h3>
                        <p className="text-sm text-gray-500">
                          Get reminders to follow up on applications
                        </p>
                      </div>
                      <Switch 
                        checked={preferences.followUpReminders} 
                        onCheckedChange={(checked) => 
                          handlePreferenceChange("followUpReminders", checked)
                        }
                      />
                    </div>
                    
                    <div className="flex items-center justify-between">
                      <div>
                        <h3 className="font-medium">Interview Preparation</h3>
                        <p className="text-sm text-gray-500">
                          Receive interview tips and preparation materials
                        </p>
                      </div>
                      <Switch 
                        checked={preferences.interviewPrep} 
                        onCheckedChange={(checked) => 
                          handlePreferenceChange("interviewPrep", checked)
                        }
                      />
                    </div>
                    
                    <div className="space-y-2">
                      <Label htmlFor="theme">Theme</Label>
                      <Select 
                        value={preferences.theme}
                        onValueChange={(value) => 
                          handlePreferenceChange("theme", value)
                        }
                      >
                        <SelectTrigger>
                          <SelectValue placeholder="Select theme" />
                        </SelectTrigger>
                        <SelectContent>
                          <SelectItem value="light">Light</SelectItem>
                          <SelectItem value="dark">Dark</SelectItem>
                          <SelectItem value="system">System</SelectItem>
                        </SelectContent>
                      </Select>
                    </div>
                  </div>
                </CardContent>
                <CardFooter className="flex justify-end">
                  <Button onClick={saveChanges} disabled={saving}>
                    {saving ? "Saving..." : "Save Preferences"}
                  </Button>
                </CardFooter>
              </Card>
            </TabsContent>
          </Tabs>
        </div>
      </main>
    </div>
  );
};

export default SettingsPage;
