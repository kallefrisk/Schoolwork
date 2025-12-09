clear

conc = zeros(7, 1); % Vektor för att förlänga datavector

load Force

f=Signal.y_values.values;

f=[f;conc]; % Förlänga vektor

% figure(1)

% plot(f)



load Acc

a=Signal.y_values.values;

a=[a;conc]; % Förlänga vektor

% figure(2)

% plot(a)

% Alla kraftsignaler (9.396 mV/N)
force=zeros(2048,10);
force(1:21,1)=(1/9.514)*f(564:564+20);
force(1:21,2)=(1/9.514)*f(5947:5947+20);
force(1:21,3)=(1/9.514)*f(10696:10696+20);
force(1:21,4)=(1/9.514)*f(15820:15820+20);
force(1:21,5)=(1/9.514)*f(20914:20914+20);
force(1:21,6)=(1/9.514)*f(27164:27164+20);
force(1:21,7)=(1/9.514)*f(31724:31724+20);
force(1:21,8)=(1/9.514)*f(36511:36511+20);
force(1:21,9)=(1/9.514)*f(41028:41028+20);
force(1:21,10)=(1/9.514)*f(45142:45142+20);

% Alla accelerometersignaler (9.730 mV/msˆ(-2))
acc=zeros(2048,10);
acc(:,1)=(1/9.396)*a(564:564+2047);
acc(:,2)=(1/9.396)*a(5947:5947+2047);
acc(:,3)=(1/9.396)*a(10696:10696+2047);
acc(:,4)=(1/9.396)*a(15820:15820+2047);
acc(:,5)=(1/9.396)*a(20914:20914+2047);
acc(:,6)=(1/9.396)*a(27164:27164+2047);
acc(:,7)=(1/9.396)*a(31724:31724+2047);
acc(:,8)=(1/9.396)*a(36511:36511+2047);
acc(:,9)=(1/9.396)*a(41028:41028+2047);
acc(:,10)=(1/9.396)*a(45142:45142+2047);


fs=256;
Ts=1/fs;
N=2048;
Ns=N*32;
t=(0:N-1)'*Ts;
ts=(0:(Ns-1)/2)';
omegak=2*pi*ts/Ns*fs;
beta=0.5;
time=exp(-beta*t)*ones(1,10);

for k=1
Acc=Ts*fft(time.*acc,Ns);
figure(k)
plot(ts*fs/Ns,20*log10(abs(Acc(1:Ns/2,k))))
Force=Ts*fft(time.*force,Ns);
figure(k+10)
plot(ts*fs/Ns,20*log10(abs(Force(1:Ns/2,k))))
H=Acc./Force;
figure(k+20)
plot(ts*fs/Ns,20*log10(abs(H(1:Ns/2,k))))
end

H_mean=sum(H,2)/10;
figure(31)
plot(omegak,20*log10(abs(H_mean(1:Ns/2))))
axis([14 16 8 13])

[maxValue, index] = max(abs(H_mean)); % Hitta maxvärdet och dess index
omegad = omegak(index); % Hitta motsvarande x-värde
%[x,y]=ginput(2);
omegaa=14.5388; %x(1);
omegab=15.6064; %x(2);

alpha=(omegab-omegaa)/2-beta

m=(omegad*omegad+beta*beta)/2/omegad/(alpha+beta)/maxValue

c=2*m*alpha

w0=sqrt(omegad*omegad+alpha*alpha)

k=m*w0*w0
